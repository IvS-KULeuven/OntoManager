<%namespace name="misc" file="../misc.mako"/>

<%inherit file="../base_layout.mako"/>


<%block name="contents">


    <div id="freeleft">

        <ul class="tree tree_root">
          % for qname, branch in U['elec']["tree"].items():
              <li>
                  ${misc.render_tree(qname, branch, "elec", qname, True, display='symbol')}
              </li>
          % endfor
        </ul>

    </div>

    <div id="freeright">

        <%
            show_type = U["elec"]["show"]["type"]
        %>

        %if show_type == "configuration":
            <%include file="Configuration.mako"/>
        %elif show_type == "IoModuleInstance":
            <%include file="IoModuleInstance.mako"/>
        %elif show_type == "IoModuleType":
            <%include file="IoModuleType.mako"/>
        %elif show_type == "DriveInstance":
            <%include file="DriveInstance.mako"/>
        %elif show_type == "DriveType":
            <%include file="DriveType.mako"/>
        %elif show_type == "ConnectorInstance":
            <%include file="ConnectorInstance.mako"/>
        %elif show_type == "ConnectorType":
            <%include file="ConnectorType.mako"/>
        %elif show_type == "DeviceType":
            <%include file="DeviceType.mako"/>
        %elif show_type == "DeviceInstance":
            <%include file="DeviceInstance.mako"/>
        %elif show_type == "ActuatorType":
            <%include file="ActuatorType.mako"/>
        %elif show_type == "ActuatorInstance":
            <%include file="ActuatorInstance.mako"/>
        %elif show_type == "SensorType":
            <%include file="SensorType.mako"/>
        %elif show_type == "SensorInstance":
            <%include file="SensorInstance.mako"/>
        %elif show_type == "SwitchType":
            <%include file="SwitchType.mako"/>
        %elif show_type == "SwitchInstance":
            <%include file="SwitchInstance.mako"/>
        %elif show_type == "MotorType":
            <%include file="MotorType.mako"/>
        %elif show_type == "MotorInstance":
            <%include file="MotorInstance.mako"/>
        %elif show_type == "PowerSupplyType":
            <%include file="PowerSupplyType.mako"/>
        %elif show_type == "PowerSupplyInstance":
            <%include file="PowerSupplyInstance.mako"/>
        %elif show_type == "Channel":
            <%include file="Channel.mako"/>
        %elif show_type == "Terminal":
            <%include file="Terminal.mako"/>
        %elif show_type == "TerminalInstance":
            <%include file="TerminalInstance.mako"/>
        %elif show_type == "PinInstance":
            <%include file="PinInstance.mako"/>
        %elif show_type == "CableType":
            <%include file="CableType.mako"/>
        %elif show_type == "CableInstance":
            <%include file="CableInstance.mako"/>
        %elif show_type == "WireInstance":
            <%include file="WireInstance.mako"/>
        %elif show_type == "CircuitBreakerInstance":
            <%include file="CircuitBreakerInstance.mako"/>
        %elif show_type == "CircuitBreakerType":
            <%include file="CircuitBreakerType.mako"/>
        %elif show_type == "CableAssemblyInstance":
            <%include file="CableAssemblyInstance.mako"/>
        %elif show_type == "CableAssemblyType":
            <%include file="CableAssemblyType.mako"/>
        %elif show_type is None:
            ## nothing to show
        %else:
            <p>No view defined for ${show_type}</p>
        %endif

    </div>

</%block>

