#!/bin/bash
ZABBIX_VERSION=V2.8.0
rm -rf *.tar.gz
echo " ${Zabbix_lan} "
if [[ "${brand}" == "KUNLUN" ]]; then
  tar zcvf KunLun_Zabbix_Template_"$ZABBIX_VERSION".tar.gz ../template_kunlun_iBMC
  sha256sum "KunLun_Zabbix_Template_$ZABBIX_VERSION".tar.gz > "KunLun_Zabbix_Template_$ZABBIX_VERSION".sha256.sum
  echo "The zabbix package is successfully generated."
else
 if [[ "${Zabbix_lan}" == "EN" ]]; then
   rm -rf ../template_customized_xfusion_iBMC_cn ../template_kunlun_iBMC
   tar zcvf xFusion_Zabbix_Template_"$ZABBIX_VERSION".tar.gz ../template_* ../README.md
   sha256sum "xFusion_Zabbix_Template_$ZABBIX_VERSION".tar.gz > "xFusion_Zabbix_Template_$ZABBIX_VERSION".sha256.sum
   echo "The zabbix package is successfully generated."
 else
   tar zcvf xFusion_Zabbix_Template_"$ZABBIX_VERSION".tar.gz ../template_customized_xfusion_iBMC_cn
   sha256sum "xFusion_Zabbix_Template_$ZABBIX_VERSION".tar.gz > "xFusion_Zabbix_Template_$ZABBIX_VERSION".sha256.sum
   echo "The zabbix package is successfully generated."
 fi
fi
