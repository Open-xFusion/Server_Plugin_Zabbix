#!/bin/bash
ZABBIX_VERSION=V2.3

rm -rf *.tar.gz
tar zcvf xFusion_Zabbix_Template_"$ZABBIX_VERSION".tar.gz ../template_* ../README.md
sha256sum "xFusion_Zabbix_Template_$ZABBIX_VERSION".tar.gz > "xFusion_Zabbix_Template_$ZABBIX_VERSION".sha256.sum
echo "The zabbix package is successfully generated."