function check(){
var cnt=0;
var q1 = document.quiz.ques1.value;
var q2 = document.quiz.ques2.value;
var q3 = document.quiz.ques3.value;
var q4 = document.quiz.ques4.value;
var q5 = document.quiz.ques5.value;
var result = document.getElementById('result')
var quiz = document.getElementById("quiz");
var per = document.getElementById("percentage");
if(q1 == "7"){
cnt++
}
if(q2 == "Network"){
cnt++
}
if(q3 == "Data Link"){
cnt++
}
if(q4 == "Transport"){
cnt++
}
if(q5 == "Presentation"){
cnt++
}
result.innerHTML = 'Total Score : ' + cnt;
per.innerHTML = 'Percentage : ' + (cnt/5)*100 + '%';

}