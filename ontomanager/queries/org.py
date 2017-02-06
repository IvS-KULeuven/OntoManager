import generic


# ====================================================== Company ==================================================

def show_Manufacturer(node, args=None):

    node.expand("org", "Manufacturer", visible=False)

    generic.fillFields(node, mandatories={ 'long_name'    : 'org:hasLongName',
                                           'short_name'   : 'org:hasShortName' })

    for manufactured in node["manufactured"]:
        node.cache[manufactured].show()

def show_Organization(node, args=None):

    node.expand("org", "Organization", visible=False)

    generic.fillFields(node, mandatories={ 'long_name'    : 'org:hasLongName',
                                           'short_name'   : 'org:hasShortName' })

    for manufactured in node["manufactured"]:
        node.cache[manufactured].show()
