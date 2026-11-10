****************************************************************************
Zabbix Plugin Pack for xFusion Device
****************************************************************************

I. General Information

    Name:     Zabbix Plugin Packsage for xFusion Server
    Function: Query, Monitoring
    Version:  2.9.20


​	
II. Description

    Integrated in the Zabbix software, xFusion Zabbix plug-in is provided as a Zabbix template. Users can directly use it or use it for secondary development. The Zabbix plug-in can be used to monitor the iBMC, HMM.


​	
III. Compatibility Information

<table>
   <tr>
      <td>Managed  Object</td>
      <td>Compatible  Zabbix Version</td>
      <td><span style="white-space:nowrap;">Version  Dependency&emsp;&emsp;&emsp;&emsp;</span></td>
      <td><span style="white-space:nowrap;">Hardware  Compatibility&emsp;&emsp;&emsp;</span></td>
      <td><span style="white-space:nowrap;">Interface  Protocol&emsp;&emsp;&emsp;&emsp;</span></td>
   </tr>
   <tr>
      <td>HMM</td>
      <td>Zabbix5.0, Zabbix5.4, Zabbix6.0</td>
      <td>HMM V686D or later</td>
      <td>Blade server: E9000(MM910)</td>
      <td>SNMP v2</td>
   </tr>
   <tr>
      <td>iBMC</td>
      <td>Zabbix5.0, Zabbix5.4, Zabbix6.0, Zabbix6.4, Zabbix7.0, Zabbix7.2, Zabbix7.4</td>
      <td>iBMC V294 or later</td>
      <td>
        Rack server: RH1288 V3, RH2288 V3, RH2288H V3, RH5885 V3, RH8100 V3, 1288H V5, 2288H V5, 2488 V5, 2288 V5, 1288H V6, <br/>
		2288H V6, 5885H V6, 1288H V7, 2288H V7, 2488H V7, 2288 V7, 5288 V7, 5885H V7, 2158H V8, 2258H V8; <br/>
	    High-density server: XH321 V3, XH620 V3, XH622 V3, XH628 V3; <br/>
	    AI server: G560 V5, G5500 V6, G5500 V7, G8600 V7, G6550 V8; <br/>
	    Blade server: CH121L V5;
      </td>
      <td>SNMP v2,SNMP v3</td>
   </tr>
   <tr>
      <td>xFusionBMC</td>
      <td>Zabbix 7.4</td>
      <td>xFusionBMC 4.01.42 or later</td>
      <td>Rack server: 2288H V8; <br/>Rack-Scale Server: DH120E V8; </td>
      <td>redfish</td>
   </tr>

</table>


​	
VI. Additional Resources

For more information consult User Guide: https://github.com/Open-xFusion/Server_Plugin_Zabbix/tree/master/docs
