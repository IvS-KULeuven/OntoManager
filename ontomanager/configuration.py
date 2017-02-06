import ConfigParser
import os
import sys
import groups


PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = os.path.join(PROJECT_DIR, "config", "config.ini")
EXAMPLE_FILE = os.path.join(PROJECT_DIR, "config", "config_example.ini")

if os.path.exists(CONFIG_FILE):
    print "Reading %s" %CONFIG_FILE
else:
    sys.exit("Expecting a configuration file: %s does not exist!\nCopy and edit example file: %s" %(CONFIG_FILE,EXAMPLE_FILE))

c = ConfigParser.ConfigParser()

c.read(CONFIG_FILE)

# read the users and groups
USERS = {}
GROUPS = {}
REPOSITORIES = {}
DEFAULT_REPOSITORY = None

for section in c.sections():
    if len(section) > len("user_"):
        if section[:len("user_")] == "user_":
            name = section[len("user_"):]
            USERS[name] = str(c.get(section, "password"))
            GROUPS[name] = []
            if c.getboolean(section, "edit"):
                GROUPS[name].append(groups.GROUP_EDITING)
            if c.getboolean(section, "view"):
                GROUPS[name].append(groups.GROUP_VIEWING)
            if c.getboolean(section, "query"):
                GROUPS[name].append(groups.GROUP_QUERYING)

            print "User: %s" %name
            print " - password: %s" %USERS[name]
            print " - groups: %s" %GROUPS[name]


    if len(section) > len("repo_"):
        if section[:len("repo_")] == "repo_":
            name = section[len("repo_"):]
            REPOSITORIES[name] = {
                "location" : str(c.get(section, "location")),
                "comment"  : str(c.get(section, "comment")),
                "name"     : str(name)
            }
            print "Repository: %s" %name
            print " - location: %s" %REPOSITORIES[name]["location"]
            print " - comment: %s" %REPOSITORIES[name]["comment"]

            if not os.path.exists(REPOSITORIES[name]["location"]):
                sys.exit("Repository %s does not exist!" %REPOSITORIES[name]["location"])

            # first location in the ini file is the default one
            if DEFAULT_REPOSITORY is None:
                DEFAULT_REPOSITORY = REPOSITORIES[name]

if DEFAULT_REPOSITORY is None:
    sys.exit("OOPS")

if not USERS.has_key("guest"):
    USERS["guest"] = "guest"
    GROUPS["guest"] = []

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
