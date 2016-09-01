/**
 * Created by NITIN KUMAR on 27-07-2016.
 */


var prev_sidebarActive_id = '1_sidebar'
    var prev_sidebarActive_no = prev_sidebarActive_id.split("_")[0]

    var prev_subjectActive_id = '1_subject'
    var prev_subjectActive_no = prev_subjectActive_id.split("_")[0]

    var prev_questionButtonNo_id = '1_s_1'
    var prev_questionButtonNo_no = prev_questionButtonNo_id.split("_")[2]

    var prev_quesActive_id = "1_question_1"
    k=0


     function sidebarActive(ctrl) {
         // id of subject is of form => '1_subject'
         // id of sidebar is of form => '1_sidebar'
         // id of question button is of form => '1_S_1'
         //id of question content is of form '1_question_1'


         var subjectActive_id = ctrl.id
         var subjectActive_no = subjectActive_id.split("_")[0]

         var sidebarActive_id = subjectActive_no + "_sidebar"
         var sidebarActive_no = sidebarActive_id.split("_")[0]


         document.getElementById(prev_subjectActive_id).className = document.getElementById(prev_subjectActive_id).className.replace(' subjectHilight', '');

         document.getElementById(prev_sidebarActive_no + "_question_" + prev_questionButtonNo_no).style.display = "none"


         document.getElementById(subjectActive_id).className += ' subjectHilight'
         document.getElementById(sidebarActive_no + "_question_1").style.display = ""


         prev_subjectActive_id = subjectActive_id
         prev_subjectActive_no = prev_subjectActive_id.split("_")[0]

         prev_sidebarActive_id = sidebarActive_id
         prev_sidebarActive_no = prev_sidebarActive_id.split("_")[0]

         prev_quesActive_id = sidebarActive_no + "_question_1"

         prev_questionButtonNo_id = sidebarActive_no + "_s_1"
         prev_questionButtonNo_no = prev_questionButtonNo_id.split("_")[2]


         questionButtonNo_text = ((parseInt(subjectActive_no) - 1) * 30) + 1


         document.getElementById("QuestionNoText").innerHTML = questionButtonNo_text

     }

