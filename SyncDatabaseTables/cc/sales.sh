#!/bin/bash
#################################################################

python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_reservation_stat_daily_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_reservation_name_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_reservation_daily_element_name_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_reservation_daily_elements_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_allotment_header_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_name_address_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_resort_room_category_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_name_owner_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_name_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_name_address_ful(dt=2019-01-30)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_country_states_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_country_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_resort_country_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_sales_ors_name_id_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'fdm.t_fdm_pms_sales_employee_ful' -f Prod -t Beta

echo -e "\033[43;31m ============================================done====================================================== \033[0m"
