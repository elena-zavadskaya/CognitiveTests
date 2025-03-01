import{_ as v,a as _,r as f,c as n,o as a,b as g,d as s,t as d,e as h,F as m,f as p,n as y,w as S,g as T,u as I}from"./index.js";const k={components:{Navbar:_},setup(){return{authStore:I()}},data(){return{testStarted:!1,testFinished:!1,timeLeft:90,timer:null,targetNumbers:[],gridNumbers:[],selectedIndexes:[],elapsedTime:0,accuracy:0,startTime:null}},computed:{formattedTime(){const t=Math.floor(this.timeLeft/60).toString().padStart(2,"0"),e=(this.timeLeft%60).toString().padStart(2,"0");return`${t}:${e}`}},methods:{startTest(){this.testStarted=!0,this.testFinished=!1,this.targetNumbers=this.generateRandomNumbers(10),this.gridNumbers=this.generateGridNumbers(100,this.targetNumbers),this.selectedIndexes=[],this.timeLeft=90,this.startTime=new Date,this.startTimer()},startTimer(){clearInterval(this.timer),this.timer=setInterval(()=>{this.timeLeft>0?this.timeLeft-=1:(clearInterval(this.timer),this.finishTest())},1e3)},generateRandomNumbers(t){const e=new Set;for(;e.size<t;)e.add(Math.floor(100+Math.random()*900));return Array.from(e)},generateGridNumbers(t,e){const r=[...e];for(;r.length<t;){const u=Math.floor(100+Math.random()*900);r.includes(u)||r.push(u)}return r.sort(()=>Math.random()-.5)},toggleCell(t){if(this.testFinished||this.timeLeft<=0)return;const e=this.selectedIndexes.indexOf(t);e!==-1?this.selectedIndexes.splice(e,1):this.selectedIndexes.push(t)},getCellClass(t){if(this.testFinished){const e=this.targetNumbers.includes(this.gridNumbers[t]);return this.selectedIndexes.includes(t)?e?"correct":"wrong":""}return this.selectedIndexes.includes(t)?"highlighted":""},finishTest(){this.testFinished=!0,clearInterval(this.timer),this.elapsedTime=90-this.timeLeft;const t=this.selectedIndexes.filter(e=>this.targetNumbers.includes(this.gridNumbers[e])).length;this.accuracy=t*10,this.saveResults()},async saveResults(){if(!this.authStore.user){alert("Пользователь не авторизован. Пожалуйста, войдите в систему.");return}const t=18,e=parseFloat(this.accuracy);if(isNaN(e)){alert("Ошибка: некорректное значение точности.");return}console.log("Отправляемые данные:",{test:t,user:this.authStore.user.id,score_percentage:e});try{const r=await fetch("http://127.0.0.1:8000/api/result/",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${localStorage.getItem("token")}`},body:JSON.stringify({test:t,user:this.authStore.user.id,score_percentage:e})});if(r.ok)alert("Результаты успешно сохранены!");else{const u=await r.json();console.error("Ошибка сервера:",u),alert(u.error||"Ошибка при сохранении результатов")}}catch(r){console.error("Ошибка при отправке результатов:",r)}}},beforeDestroy(){clearInterval(this.timer)}},C={class:"container mt-5 text-center"},w={id:"app"},x={key:0},F={key:1},L={class:"numbers-row"},M={class:"grid"},B=["onClick"],D={key:2,class:"end-message"};function R(t,e,r,u,i,o){const b=f("Navbar"),N=f("router-link");return a(),n(m,null,[g(b),s("div",C,[s("h2",null,d(t.$route.params.name),1),s("div",w,[!i.testStarted&&!i.testFinished?(a(),n("div",x,[e[2]||(e[2]=s("h1",null,"Тест на избирательность внимания",-1)),e[3]||(e[3]=s("p",null," Вы увидите перед собой список из 10 трехзначных чисел, а ниже таблицу из 100 ячеек с трехзначными числами. Ваша задача — как можно быстрее найти и выделить эти 10 чисел. ",-1)),s("button",{class:"start-button btn btn-primary",onClick:e[0]||(e[0]=(...l)=>o.startTest&&o.startTest(...l))},"Начать")])):i.testStarted?(a(),n("div",F,[s("p",null,"Оставшееся время: "+d(o.formattedTime),1),s("div",null,[e[4]||(e[4]=s("h2",null,"Заданные числа:",-1)),s("div",L,[(a(!0),n(m,null,p(i.targetNumbers,(l,c)=>(a(),n("span",{key:c},d(l),1))),128))])]),s("div",M,[(a(!0),n(m,null,p(i.gridNumbers,(l,c)=>(a(),n("div",{key:c,class:y(o.getCellClass(c)),onClick:V=>o.toggleCell(c)},d(l),11,B))),128))]),i.timeLeft>0?(a(),n("button",{key:0,onClick:e[1]||(e[1]=(...l)=>o.finishTest&&o.finishTest(...l)),class:"btn btn-success mt-3"},"Готово")):h("",!0)])):h("",!0),i.testFinished?(a(),n("div",D,[e[5]||(e[5]=s("h3",null,"Тест завершен!",-1)),s("p",null,"Время выполнения: "+d(i.elapsedTime)+" секунд",1),s("p",null,"Точность: "+d(i.accuracy)+"%",1)])):h("",!0),g(N,{to:"/tests",class:"btn btn-secondary"},{default:S(()=>e[6]||(e[6]=[T("Назад к тестам")])),_:1})])])],64)}const A=v(k,[["render",R],["__scopeId","data-v-73b3c0a8"]]);export{A as default};
