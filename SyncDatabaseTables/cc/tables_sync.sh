#!/bin/bash
#################################################################


python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_enrolment_channel_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================11====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_enrolment_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================12====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_membership_country_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================13====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_membership_kpi_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================14====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_contribution_channel_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================15====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_contribution_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================16====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_feeder_market_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================17====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_loyalty_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================18====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_loyalty_member_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================19====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_loyalty_visitor_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================20====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_visitor_stay_repeat_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================21====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_rooms_market_position_summary_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================22====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_rooms_otb_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================23====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_loyalty_member_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================24====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_redemption_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================25====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_unique_redeemers_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================26====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_gc_summary_visitor_stay_stat_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================27====================================================== \033[0m"

#依赖表
python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_gc_award_type' -f Prod -t Beta
echo -e "\033[43;31m ============================================35====================================================== \033[0m"

