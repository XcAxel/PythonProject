#!/bin/bash
#################################################################
#fin
python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_fb_outlet_department_outlet_detail_info' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_fb_outlet_info' -f Prod -t Beta
echo -e "\033[43;31m ============================================30====================================================== \033[0m"
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_fb_hotel_ful' -f Prod -t Beta
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_fb_hotel_budget_exchange_rate_ful' -f Prod -t Beta
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_pnl_hotel_ful' -f Prod -t Beta
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_gop_hotel_budget_exchange_rate' -f Prod -t Beta
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_rooms_hotel_ful' -f Prod -t Beta
#python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_rooms_hotel_budget_exchange_rate' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_fb_hotel_exchange_rate_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_pnl_hotel_exchange_rate_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_fin_rooms_hotel_exchange_rate_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================31====================================================== \033[0m"

#app
python /home/q/www/tools/hive_table_sync.py -T 'cdm.d_cdm_otb_source' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.d_cdm_otb_channel' -f Prod -t Beta
echo -e "\033[43;31m ============================================0======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_app_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================1======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_app_production_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================2======================================================= \033[0m"

#rooms
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_rooms_market_position_summary_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================3======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.d_cdm_otb_market_hotel' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_rooms_otb_hotel_ful' -f Prod -t Beta
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_rooms_otb_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================4======================================================= \033[0m"

#bsc
python /home/q/www/tools/hive_table_sync.py -T 'cdm.d_cdm_otb_source_bsc' -f Prod -t Beta

python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_bsc_channel_detail_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================5======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_bsc_benchmarking_score_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================6=======================================================\033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_bsc_fin_detail_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================7======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_bsc_guest_score_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================8======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_bsc_hotel_score_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================9======================================================= \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'cdm.t_cdm_bsc_rate_parity_ful' -f Prod -t Beta
echo -e "\033[43;31m ============================================10====================================================== \033[0m"

#gc
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
python /home/q/www/tools/hive_table_sync.py -T 'ods.t_ods_outlet_operating_hr_hotel(dt=2018-01-22)' -f Prod -t Beta
echo -e "\033[43;31m ============================================28====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_quarter_hotel' -f Prod -t Beta
echo -e "\033[43;31m ============================================32====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_market_hotel' -f Prod -t Beta
echo -e "\033[43;31m ============================================33====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_hotel_profile_info' -f Prod -t Beta
echo -e "\033[43;31m ============================================34====================================================== \033[0m"
python /home/q/www/tools/hive_table_sync.py -T 'edw.d_edw_gc_award_type' -f Prod -t Beta
echo -e "\033[43;31m ============================================35====================================================== \033[0m"

echo -e "\033[43;31m ============================================== Done ================================================ \033[0m"
