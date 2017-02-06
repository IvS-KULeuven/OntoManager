__author__ = 'wimpe'

from queries import sys, browse, soft, elec, org, man, colors
from queries.register import REGISTRY, RegAND


REGISTRY.registerView( "browse" , "resource"    , "rdfs:Resource"           , browse.show_browse  )
REGISTRY.registerView( "browse" , "class"       , "owl:Class"               , browse.show_browse  )
REGISTRY.registerView( "browse" , "thing"       , "owl:Thing"               , browse.show_browse  )
# organizations
REGISTRY.registerView( "org"    , "Organization"     , "org:Organization"             , org.show_Organization    ,   [ ["manufactured"   , man.getManufactured    ] ] )
REGISTRY.registerView( "org"    , "Manufacturer"     , "man:Manufacturer"             , org.show_Manufacturer    ,   [ ["manufactured"   , man.getManufactured    ] ] )
REGISTRY.registerView( "colors"    , "Color"     , "colors:Color"             , colors.show_Color ,   [] )

REGISTRY.registerView(  "sys"   , "Realization" , "sys:Realization"         , sys.show_Realization,   [ ["realizes"       , sys.getRealizes        ] ] )
REGISTRY.registerView( "sys"    , "project"     , "dev:Project"             , sys.show_project    ,   [ ["concepts"       , sys.getConcepts         ] ] )
REGISTRY.registerView(  "sys"   , "concept"     , "dev:Concept"             , sys.show_concept    ,   [ ["requirements"   , sys.getRequirements     ],
                                                                                                        ["states"         , sys.getStates           ],
                                                                                                        ["properties"     , sys.getProperties       ],
                                                                                                        ["constraints"    , sys.getConstraints      ],
                                                                                                        ["tests"          , sys.getTests            ],
                                                                                                        ["designs"        , sys.getDesigns          ] ])
REGISTRY.registerView(  "sys"   , "design"      , "dev:Design"              , sys.show_design     ,   [ ["realizes"       , sys.getRealizes         ],
                                                                                                        ["requirements"   , sys.getRequirements     ],
                                                                                                        ["realized_requirements", sys.getRealizedRequirements ],
                                                                                                        ["states"         , sys.getStates           ],
                                                                                                        ["properties"     , sys.getProperties       ],
                                                                                                        ["constraints"    , sys.getConstraints      ],
                                                                                                        ["tests"          , sys.getTests            ],
                                                                                                        ["parts"          , sys.getParts            ] ])
REGISTRY.registerView(  "sys"   , "test"        , "dev:Test"                , sys.show_test       ,   [ ["verifies"       , sys.getVerifies         ],
                                                                                                        ["tests"          , sys.getTested           ]] )
REGISTRY.registerView(  "sys"   , "requirement" , "dev:Requirement"         , sys.show_requirement,   [ ["derives"        , sys.getDerives          ],
                                                                                                        ["derived_from"   , sys.getDerivedFrom      ],
                                                                                                        ["declared_by"    , sys.getDeclaredBy       ],
                                                                                                        ["satisfied_by"   , sys.getSatisfiedBy      ] ])

# elec
REGISTRY.registerView( "elec"    , "Gender"     , "elec:Gender"             , elec.show_Gender ,   [] )
REGISTRY.registerView( "elec"   , "configuration","elec:Configuration"      , elec.show_configuration,[ ["I/O modules"    , elec.getIoModuleInstances ],
                                                                                                        ["circuit breakers", elec.getCircuitBreakerInstances ],
                                                                                                        ["power supplies" , elec.getPowerSupplyInstances ],
                                                                                                        ["motors"         , elec.getMotorInstances ],
                                                                                                        ["drives"         , elec.getDriveInstances ],
                                                                                                        ["terminals"      , elec.getTerminals ],
                                                                                                        ["wires"          , elec.getWires ],
                                                                                                        ["connectors"     , elec.getConnectors ],
                                                                                                        ["sensors"        , elec.getSensorInstances ],
                                                                                                        ["actuators"      , elec.getActuatorInstances ],
                                                                                                        ["switches"       , elec.getSwitchInstances ],
                                                                                                        ["cables"         , elec.getCables ],
                                                                                                        ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                        ["sub-configurations"       , elec.getSubConfigurations ],
                                                                                                        ["other devices"        , elec.getOtherDeviceInstances ] ])
REGISTRY.registerView( "elec"   , "DeviceType" , "elec:DeviceType"       , elec.show_DeviceType,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                          ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "DeviceInstance","elec:DeviceInstance", elec.show_DeviceInstance,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ]])
REGISTRY.registerView( "elec"   , "CableType" , "elec:CableType"       , elec.show_CableType,           [ ["wires"          , elec.getWires ],
                                                                                                          ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "ActuatorType" , "elec:ActuatorType"       , elec.show_ActuatorType,  [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"          , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                          ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "SensorType"   , "elec:SensorType"         , elec.show_SensorType,    [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                          ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "PowerSupplyType", "elec:PowerSupplyType"  , elec.show_PowerSupplyType,[ ["channels"       , elec.getChannels ],
                                                                                                           ["terminals"      , elec.getTerminals ],
                                                                                                           ["wires"           , elec.getWires ],
                                                                                                           ["cables"         , elec.getCables ],
                                                                                                           ["connectors"     , elec.getConnectors],
                                                                                                           ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                           ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "SwitchType"   , "elec:SwitchType"         , elec.show_SwitchType,    [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                          ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "IoModuleType" ,"elec:IoModuleType"       , elec.show_IoModuleType, [ ["channels"       , elec.getChannels ],
                                                                                                        ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                        ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "IoModuleInstance","elec:IoModuleInstance", elec.show_IoModuleInstance, [ ["channels"       , elec.getChannels ],
                                                                                                            ["terminals"      , elec.getTerminals ],
                                                                                                            ["wires"          , elec.getWires ],
                                                                                                            ["satisfies"      , sys.getSatisfies ] ])
REGISTRY.registerView( "elec"   , "CircuitBreakerType" ,"elec:CircuitBreakerType"       , elec.show_CircuitBreakerType, [ ["channels"       , elec.getChannels ],
                                                                                                        ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                        ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "CircuitBreakerInstance","elec:CircuitBreakerInstance", elec.show_CircuitBreakerInstance, [ ["channels"       , elec.getChannels ],
                                                                                                            ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                            ["satisfies"      , sys.getSatisfies ] ])
REGISTRY.registerView( "elec"   , "DriveType" , "elec:DriveType"       , elec.show_DriveType,           [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                        ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "MotorType" , "elec:MotorType"       , elec.show_MotorType,           [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                        ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "CableAssemblyType" , "elec:CableAssemblyType"       , elec.show_CableAssemblyType,
                                                                                                        [ ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "CableInstance","elec:CableInstance", elec.show_CableInstance,        [ ["wires"       , elec.getWires ]])
REGISTRY.registerView( "elec"   , "SensorInstance","elec:SensorInstance", elec.show_SensorInstance,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ]])
REGISTRY.registerView( "elec"   , "ActuatorInstance","elec:ActuatorInstance", elec.show_ActuatorInstance,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ]])
REGISTRY.registerView( "elec"   , "PowerSupplyInstance","elec:PowerSupplyInstance", elec.show_PowerSupplyInstance,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ]])
REGISTRY.registerView( "elec"   , "SwitchInstance","elec:SwitchInstance", elec.show_SwitchInstance,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ]])
REGISTRY.registerView( "elec"   , "MotorInstance","elec:MotorInstance", elec.show_MotorInstance,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ]])
REGISTRY.registerView( "elec"   , "DriveInstance","elec:DriveInstance", elec.show_DriveInstance,        [ ["channels"       , elec.getChannels ],
                                                                                                          ["terminals"      , elec.getTerminals ],
                                                                                                          ["wires"           , elec.getWires ],
                                                                                                          ["cables"         , elec.getCables ],
                                                                                                          ["cable assemblies", elec.getCableAssemblyInstances ],
                                                                                                          ["connectors"     , elec.getConnectors]])
REGISTRY.registerView( "elec"   , "CableAssemblyInstance","elec:CableAssemblyInstance", elec.show_CableAssemblyInstance,
                                                                                                        [ ["cables"         , elec.getCables ],
                                                                                                          ["connectors"     , elec.getConnectors]])
REGISTRY.registerView( "elec"   , "Channel"      ,"elec:Channel"            , elec.show_Channel,        [ ["terminals"      , elec.getTerminals ] ])
REGISTRY.registerView( "elec"   , "ConnectorType"       ,"elec:ConnectorType"     , elec.show_ConnectorType,  [ ["pins"           , elec.getTerminals ],
                                                                                                                ["fits"           , elec.getFits ],
                                                                                                                ["owning_configurations", elec.getOwningConfigurations ] ])
REGISTRY.registerView( "elec"   , "ConnectorInstance"   ,"elec:ConnectorInstance" , elec.show_ConnectorInstance,  [ ["pins"         , elec.getTerminals ],
                                                                                                                    ["wires"        , elec.getWires] ])
REGISTRY.registerView( "elec"   , "Terminal"            ,"elec:Terminal"           , elec.show_Terminal,            [ ["connections"    , elec.getConnections ],
                                                                                                                      ["all_connections", elec.getAllConnections ] ] )
REGISTRY.registerView( "elec"   , "TerminalInstance"     ,"elec:TerminalInstance"  , elec.show_TerminalInstance,   [ ["connections"    , elec.getConnections ],
                                                                                                                      ["all_connections", elec.getAllConnections ] ] )
REGISTRY.registerView( "elec"   , "Wire"          ,"elec:Wire"                , elec.show_Wire,          [["colors"         , colors.getColors ],
                                                                                                          ["connections"    , elec.getConnections ]] )
REGISTRY.registerView( "elec"   , "WireInstance"  ,"elec:WireInstance"        , elec.show_WireInstance,    [ ["colors"         , colors.getColors ],["connections"    , elec.getConnections ] ] )

# soft
REGISTRY.registerView( "soft"   , "primitive"   , "expr:Primitive"          , soft.show_primitive  )
REGISTRY.registerView(  "soft"  , "namespace"   , "soft:Namespace"          , soft.show_namespace   , [ ["namespaces"     , soft.getNamespaces      ],
                                                                                                        ["FBs"            , soft.getFBs             ],
                                                                                                        ["STRUCTs"        , soft.getStructs         ],
                                                                                                        ["ENUMs"          , soft.getEnums           ] ] )
REGISTRY.registerView(  "soft"  , "library"     , "soft:Library"            , soft.show_library   ,   [ ["namespaces"     , soft.getNamespaces      ],
                                                                                                        ["FBs"            , soft.getFBs             ],
                                                                                                        ["STRUCTs"        , soft.getStructs         ],
                                                                                                        ["ENUMs"          , soft.getEnums           ] ] )
REGISTRY.registerView(  "soft"  , "variable"    , "soft:Variable"           , soft.show_variable    , [ ["realizes"       , sys.getRealizes         ],
                                                                                                        ["qualifiers"     , soft.getQualifiers      ],
                                                                                                        ["links"          , soft.getLinks           ],
                                                                                                        ["member_of"      , soft.getMemberOf        ]])
REGISTRY.registerView(  "soft"  , "attribute"   , "soft:Attribute"          , soft.show_attribute   , [ ["realizes"       , sys.getRealizes         ],
                                                                                                        ["qualifiers"     , soft.getQualifiers      ],
                                                                                                        ["links"          , soft.getLinks           ],
                                                                                                        ["member_of"      , soft.getMemberOf        ]])
REGISTRY.registerView(  "soft"  , "argument"    , "soft:Argument"           , soft.show_argument    , [ ["realizes"       , sys.getRealizes         ],
                                                                                                        ["qualifiers"     , soft.getQualifiers      ],
                                                                                                        ["links"          , soft.getLinks           ],
                                                                                                        ["member_of"      , soft.getMemberOf        ]])
REGISTRY.registerView(  "soft"  , "type"        , "soft:Type"               , soft.show_type        )
REGISTRY.registerView(  "soft"  , "plc_method"  , "iec61131:Method"         , soft.show_plc_method  , [ ["var_in"         , soft.getInputVariables  ],
                                                                                                        ["var_out"        , soft.getOutputVariables ],
                                                                                                        ["var_inout"      , soft.getInOutVariables  ],
                                                                                                        ["var_local"      , soft.getLocalVariables  ],
                                                                                                        ["member_of"      , soft.getMemberOf        ] ])
REGISTRY.registerView(  "soft"  , "fb"          , "iec61131:FunctionBlock"  , soft.show_fb          , [ ["var_in"         , soft.getInputVariables  ],
                                                                                                        ["var_out"        , soft.getOutputVariables ],
                                                                                                        ["var_inout"      , soft.getInOutVariables  ],
                                                                                                        ["var_local"      , soft.getLocalVariables  ],
                                                                                                        ["methods"        , soft.getMethods         ] ] )
REGISTRY.registerView(  "soft"  , "struct"      , "iec61131:Struct"         , soft.show_struct      , [ ["attributes"     , soft.getAttributes      ] ] )
REGISTRY.registerView(  "soft"  , "enum"        , "soft:Enumeration"        , soft.show_enum        , [ ["items"          , soft.getEnumItems       ] ] )
REGISTRY.registerView(  "soft"  , "enum_item"   , "soft:EnumerationItem"    , soft.show_enum_item   )
REGISTRY.registerView(  "soft"  , "implementation", "soft:Implementation"   , soft.show_implementation, [ ["expressions"  , soft.getImplementationExpressions   ]])
REGISTRY.registerView(  "soft"  , "var_in"      , "iec61131:InputVariable"  , soft.show_variable    , [ ["qualifiers"     , soft.getQualifiers      ],
                                                                                                        ["member_of"      , soft.getMemberOf        ]])
REGISTRY.registerView(  "soft"  , "var_out"     , "iec61131:OutputVariable" , soft.show_variable    , [ ["qualifiers"     , soft.getQualifiers      ],
                                                                                                        ["member_of"      , soft.getMemberOf        ]])
REGISTRY.registerView(  "soft"  , "var_inout"   , "iec61131:InOutVariable"  , soft.show_variable    , [ ["qualifiers"     , soft.getQualifiers      ],
                                                                                                        ["member_of"      , soft.getMemberOf        ]])
REGISTRY.registerView(  "soft"  , "var_local"   , "iec61131:LocalVariable"  , soft.show_variable    , [ ["qualifiers"     , soft.getQualifiers      ],
                                                                                                        ["member_of"      , soft.getMemberOf        ]])
REGISTRY.registerView(  "soft"  , "qualifier"   , "soft:Qualifier"          , soft.show_qualifier   )
REGISTRY.registerView(  "soft"  , "if_then"     , "soft:IfThen"             , soft.show_if_then     )
REGISTRY.registerView(  "soft"  , "call"        , "soft:Call"               , soft.show_call        , [ ["assignments"     , soft.getAssignments    ]])
REGISTRY.registerView(  "soft"  , "unary_op"    , "expr:UnaryOperation"     , soft.show_unary_op    )
REGISTRY.registerView(  "soft"  , "binary_op"   , "expr:BinaryOperation"    , soft.show_binary_op   )
REGISTRY.registerView(  "soft"  , "operator"    , "expr:Operator"           , soft.show_operator    )
REGISTRY.registerView(  "soft"  , "Interface"   , "soft:Interface"          , soft.show_Interface  , [ ["variables"         , soft.getInterfaceVariables ] ])
REGISTRY.registerView(  "soft"  , "InterfaceInstance"   , "soft:InterfaceInstance"          , soft.show_InterfaceInstance  , [ ["variables"         , soft.getInterfaceInstanceVariables ] ])

