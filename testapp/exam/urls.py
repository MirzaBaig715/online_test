from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('exam.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'user_login'),
    url(r'^start/$', 'start'),
    url(r'^quit/$', 'quit'),
    url(r'^intro/$','start'),
    url(r'^complete/$', 'complete'),
    url(r'^register/$', 'user_register'),
    url(r'^(?P<q_id>\d+)/$', 'question'),
    url(r'^(?P<q_id>\d+)/check/$', 'check'),


    url(r'^manage/$', 'prof_manage'),
    url(r'^manage/addquestion/$', 'add_question'),
    url(r'^manage/addquestion/(?P<question_id>\d+)/$', 'add_question'),    
    url(r'^manage/addquiz/$', 'add_quiz'),
    url(r'^manage/editquiz/$', 'edit_quiz'),
    url(r'^manage/editquestion/$', 'edit_question'),
    url(r'^manage/addquiz/(?P<quiz_id>\d+)/$', 'add_quiz'),
    url(r'^manage/gradeuser/$', 'show_all_users'),
    url(r'^manage/gradeuser/(?P<username>[a-zA-Z0-9_.]+)/$', 'grade_user'),
    url(r'^manage/questions/$', 'show_all_questions'),
    url(r'^manage/showquiz/$','show_all_quiz'),   
    url(r'^manage/monitor/$', 'monitor'),
    url(r'^manage/showquestionpapers/$','show_all_questionpapers'),  
    url(r'^manage/showquestionpapers/(?P<questionpaper_id>\d+)/$', 'show_all_questionpapers'),
    url(r'^manage/monitor/(?P<quiz_id>\d+)/$', 'monitor'),    
    url(r'^manage/user_data/(?P<username>[a-zA-Z0-9_.]+)/$', 'user_data'),
    url(r'^manage/designquestionpaper/$','design_questionpaper'),
    url(r'^manage/designquestionpaper/(?P<questionpaper_id>\d+)/$', 'design_questionpaper'),
    url(r'^manage/designquestionpaper/automatic/(?P<questionpaper_id>\d+)/$','automatic_questionpaper'),
    url(r'^manage/designquestionpaper/automatic$','automatic_questionpaper'),
    url(r'^manage/designquestionpaper/manual$','manual_questionpaper'),

)

