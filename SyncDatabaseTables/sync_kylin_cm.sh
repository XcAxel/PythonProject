#!/bin/bash
#################################################################
#hotel_info
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_edw_hotel_profile_info --cube=c_edw_hotel_profile_info_2 -f Prod -t Beta

#fin
#y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_fb_hotel_detail_ful --cube=c_cdm_fin_fb_hotel_add_index_new_1 -f Prod -t Beta
#y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_fb_hotel_budget_exchange_rate_detail_ful --cube=c_cdm_fin_fb_hotel_budget_exchange_rate_new_1 -f Prod -t Beta
#y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_pnl_hotel_diff_add_index_new --cube=c_cdm_fin_pnl_hotel_add_index_new_1 -f Prod -t Beta
#y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_gop_hotel_budget_exchange_rate --cube=c_cdm_fin_pnl_hotel_budget_exchange_rate_new_1 -f Prod -t Beta
#y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_rooms_hotel_diff_budget_add_index_new --cube=c_edw_fin_rooms_hotel_add_index_new_1 -f Prod -t Beta
#y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_rooms_hotel_budget_exchange_rate --cube=c_cdm_fin_rooms_hotel_budget_exchange_rate_new_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_fb_hotel_budget_exchange_rate_view_ful --cube=c_cdm_fin_fb_hotel_budget_exchange_rate_view_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_fb_hotel_normal_exchange_rate_view_ful --cube=c_cdm_fin_fb_hotel_normal_exchange_rate_view_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_pnl_hotel_budget_exchange_rate_view_ful --cube=c_cdm_fin_pnl_hotel_budget_exchange_rate_view_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_pnl_hotel_normal_exchange_rate_view_ful --cube=c_cdm_fin_pnl_hotel_normal_exchange_rate_view_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_rooms_hotel_budget_exchange_rate_view_ful --cube=c_cdm_fin_rooms_hotel_budget_exchange_rate_view_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_fin_rooms_hotel_normal_exchange_rate_view_ful --cube=c_cdm_fin_rooms_hotel_normal_exchange_rate_view_ful_1 -f Prod -t Beta

#rooms
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_rooms_otb_hotel_market_ful --cube=c_cdm_rooms_otb_hotel_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_rooms_otb_ful_add_index --cube=c_cdm_rooms_otb_ful_add_index_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_rooms_market_position_summary_ful --cube=c_cdm_rooms_market_position_summary_ful_1 -f Prod -t Beta

#gc
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_loyalty_ful --cube=c_cdm_gc_summary_loyalty_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_feeder_market_ful --cube=c_cdm_gc_summary_feeder_market_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_redemption_ful_add_index --cube=c_cdm_gc_redemption_ful_add_index_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_unique_redeemers_ful_index_add --cube=c_cdm_gc_unique_redeemers_ful_add_index_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_redemption_ful --cube=c_cdm_gc_summary_redemption_ful_2 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_unique_redeemers_ful_add_index_new --cube=c_cdm_gc_summary_unique_redeemers_ful_2 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_contribution_channel_ful --cube=c_cdm_gc_summary_contribution_channel_ful_2 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_contribution_ful --cube=c_cdm_gc_summary_contribution_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_membership_kpi_ful --cube=c_cdm_gc_membership_kpi_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_enrolment_ful_add_index --cube=c_cdm_gc_enrolment_ful_add_index_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_loyalty_member_ful --cube=c_cdm_gc_summary_loyalty_member_ful_2 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_loyalty_visitor_ful --cube=c_cdm_gc_summary_loyalty_visitor_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_enrolment_channel_ful --cube=c_cdm_gc_enrolment_channel_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_membership_country_ful --cube=c_cdm_gc_membership_country_ful_1 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_visitor_stay_stat_ful --cube=c_cdm_gc_summary_visitor_stay_stat_ful_2 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_gc_summary_loyalty_visitor_stay_repeat_ful --cube=c_cdm_gc_summary_loyalty_visitor_stay_repeat_2 -f Prod -t Beta

#app
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_app_ful --cube=c_cdm_app_ful_2 -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_app_production --cube=c_cdm_app_production_1 -f Prod -t Beta

#bsc
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_bsc_rate_parity_ful --cube=c_cdm_bsc_rate_parity_ful -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_bsc_hotel_score_kpi_ful --cube=c_cdm_bsc_hotel_score_kpi_ful -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_bsc_guest_score_ful --cube=c_cdm_bsc_guest_score_ful -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_bsc_fin_detail_ful --cube=c_cdm_bsc_fin_detail_ful -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_bsc_channel_details_ful_bsc --cube=c_cdm_bsc_channel_details_ful_bsc -f Prod -t Beta
y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_cdm_bsc_benchmarking_score_ful --cube=c_cdm_bsc_benchmarking_score_ful -f Prod -t Beta



#运营时间
#y | python /home/q/www/tools/kylin_meta_sync.py -m -c --project=data_center_test --model=m_ods_outlet_operating_hr_hotel --cube=c_ods_outlet_operating_hr_hotel -f Prod -t Beta

echo -e "\033[43;31m ============================================== Done ================================================ \033[0m"
