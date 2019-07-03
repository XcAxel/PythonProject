#!/bin/bash
#################################################################
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_fb_hotel_ful' -f Prod -t Beta
#echo -e "\033[43;31m ============================================1======================================================= \033[0m"
#python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_hotel_profile_info_fin_add_index_view' -f Prod -t Beta
#echo -e "\033[43;31m ============================================2======================================================= \033[0m"
#python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_quarter_hotel' -f Prod -t Beta
#echo -e "\033[43;31m ============================================3======================================================= \033[0m"
#python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_fb_outlet_department_outlet_detail_info' -f Prod -t Beta
#echo -e "\033[43;31m ============================================4======================================================= \033[0m"
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_pnl_hotel_ful' -f Prod -t Beta
#echo -e "\033[43;31m ============================================5======================================================= \033[0m"
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_rooms_hotel_ful' -f Prod -t Beta
#echo -e "\033[43;31m ============================================6=======================================================\033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_rooms_hotel_budget_exchange_rate(dt=2018-12-02)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_rooms_hotel_budget_exchange_rate(dt=2019-01-02)' -f Prod -t Beta
echo -e "\033[43;31m ============================================7======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_gop_hotel_budget_exchange_rate(2018-12-02)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_gop_hotel_budget_exchange_rate(2019-01-02)' -f Prod -t Beta
echo -e "\033[43;31m ============================================8======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_fb_hotel_budget_exchange_rate_ful(2018-12-02)' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_fb_hotel_budget_exchange_rate_ful(2019-01-02)' -f Prod -t Beta
echo -e "\033[43;31m ============================================9======================================================= \033[0m"

echo -e "\033[43;31m ============================================done====================================================== \033[0m"
