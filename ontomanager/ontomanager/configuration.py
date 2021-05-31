import configparser
import os
import sys
from . import groups

# construct some paths
PROJECT_DIR  = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE  = os.path.join(PROJECT_DIR, "../config", "config.ini")
EXAMPLE_FILE = os.path.join(PROJECT_DIR, "../config", "config_example.ini")

# check if the config file exists
if os.path.exists(CONFIG_FILE):
    print(("Reading %s" %CONFIG_FILE))
else:
    sys.exit("Expecting a configuration file: %s does not exist!\nCopy and edit example file: %s" %(CONFIG_FILE,EXAMPLE_FILE))

# read the config
c = configparser.ConfigParser()
c.read(CONFIG_FILE)

# get the coffeescript executable
print("Reading the coffeescript executable:")
try:
    COFFEE = c.get("general", "coffee")
    print(("Coffeescript exectutable: %s" %COFFEE))
except Exception as e:
    print("No coffeescript executable was mentioned in the configuration file (config/config.ini)")
    print("Look at the example_config.ini for an example of this entry")
    raise e

# get the loglevel
print("Reading the LOGLEVEL:")
try:
    LOGLEVEL = c.get("general", "loglevel")
    print(("LOGLEVEL: %s" %LOGLEVEL))
except Exception as e:
    print("No LOGLEVEL was mentioned in the configuration file (config/config.ini)")
    print("Look at the example_config.ini for an example of this entry")
    raise e

# read the users, groups, home directories, and repositories
USERS = {}
GROUPS = {}
HOMES = {}
REPOSITORIES = {}

# create a pointer to the first mentioned repository = the default repository
DEFAULT_REPOSITORY = None

# loop trough the sections, and search for user_ and repo_ prefixes
for section in c.sections():

    # users
    # ====
    if len(section) > len("user_"):
        if section[:len("user_")] == "user_":
            name = section[len("user_"):]
            USERS[name] = str(c.get(section, "password"))
            try:
                HOMES[name] = str(c.get(section, "home"))
            except:
                HOMES[name] = None
            GROUPS[name] = []
            if c.getboolean(section, "edit"):
                GROUPS[name].append(groups.GROUP_EDITING)
            if c.getboolean(section, "view"):
                GROUPS[name].append(groups.GROUP_VIEWING)
            if c.getboolean(section, "query"):
                GROUPS[name].append(groups.GROUP_QUERYING)

            print("User: %s" %name)
            print(" - password: %s" %USERS[name])
            print(" - groups: %s" %GROUPS[name])
            print(" - home: %s" %HOMES[name])

    # repositories
    # ============
    if len(section) > len("repo_"):
        if section[:len("repo_")] == "repo_":
            name = section[len("repo_"):]
            REPOSITORIES[name] = {
                "ontologies_dir" : str(c.get(section, "ontologies_dir")),
                "coffee_dir"     : str(c.get(section, "coffee_dir")),
                "generated_dir"  : str(c.get(section, "generated_dir")),
                "comment"        : str(c.get(section, "comment")),
                "name"           : str(name)
            }
            print("Repository: %s" %name)
            print(" - ontologies_dir: %s" %REPOSITORIES[name]["ontologies_dir"])
            print(" - coffee_dir: %s" %REPOSITORIES[name]["coffee_dir"])
            print(" - generated_dir: %s" %REPOSITORIES[name]["generated_dir"])
            print(" - comment: %s" %REPOSITORIES[name]["comment"])

            if not os.path.exists(REPOSITORIES[name]["ontologies_dir"]):
                sys.exit("Repository %s is invalid: directory %s does not exist!" %(name, REPOSITORIES[name]["ontologies_dir"]))

            if not os.path.exists(REPOSITORIES[name]["coffee_dir"]):
                sys.exit("Repository %s is invalid: directory %s does not exist!" %(name, REPOSITORIES[name]["coffee_dir"]))

            if not os.path.exists(REPOSITORIES[name]["generated_dir"]):
                sys.exit("Repository %s is invalid: directory %s does not exist!" %(name, REPOSITORIES[name]["generated_dir"]))

            # first location in the ini file is the default one
            if DEFAULT_REPOSITORY is None:
                DEFAULT_REPOSITORY = REPOSITORIES[name]

# there must be at least one user mentioned
if DEFAULT_REPOSITORY is None:
    sys.exit("No user with repository mentioned in the config.ini!")

# if there is no user 'guest' mentioned, we create this user ourselves
if "guest" not in USERS:
    USERS["guest"] = "guest"
    GROUPS["guest"] = []

# define a function to get the groups of a particular user
def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
