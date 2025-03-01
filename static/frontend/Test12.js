import{_ as w,a as g,r as h,c as r,o as i,b as m,d as o,t as d,e as u,F as f,f as y,w as b,g as _,u as T}from"./index.js";const x={components:{Navbar:g},setup(){return{authStore:T()}},data(){return{words:["ФАКТ","ТЕОРИЯ","БИЗНЕС","ДОЧИСЛО","КАРТЕ","МАРКЕТИНГ","ДАННЫЕ","ДЕНЬГИ","КЛЮЧ","КУСТ","АНАЛИЗ","ДИАГНОЗ","ПРОБЛЕМА","РЕШЕНИЕ","ПЛАН","КОНЦЕПЦИЯ","СТРАТЕГИЯ","МОДЕЛЬ","ИССЛЕДОВАНИЕ","РЕСУРС","ИНФОРМАЦИЯ","ПРОЦЕСС","СИСТЕМА","КОММУНИКАЦИЯ","ПАРТНЁР","ПРОЕКТ","УСПЕХ","ДИАЛОГ","КОНТРОЛЬ","ОЦЕНКА"],randomText:"",foundCount:null,options:[],selectedOption:null,feedback:"",isAnswered:!1,testStarted:!1,time:0,accuracy:0}},methods:{startTest(){this.testStarted=!0,this.startTime=Date.now(),this.generateRandomText()},generateRandomText(){let e="";const s=new Set;for(;e.length<350&&s.size!==this.words.length;){const a=this.words[Math.floor(Math.random()*this.words.length)];if(!s.has(a)){s.add(a);const n=Math.floor(Math.random()*(e.length+1));e=this.insertWord(a,e,n)}}for(;e.length<350;)e+=" ";this.randomText=e.trim()},insertWord(e,t,s){return t.slice(0,s)+e+t.slice(s)},checkWords(){const e=new RegExp(this.words.join("|"),"g");this.foundCount=(this.randomText.match(e)||[]).length,this.generateOptions()},generateOptions(){const e=this.foundCount,t=new Set([e]);for(;t.size<4;){const s=Math.floor(Math.random()*(this.words.length+1));t.add(s)}this.options=Array.from(t).sort((s,a)=>s-a)},checkAnswer(e){this.selectedOption=e,e===this.foundCount?this.feedback="Правильно!":this.feedback="Попробуйте снова, неверно.",this.isAnswered=!0,this.calculateResults()},calculateResults(){const e=(Date.now()-this.startTime)/1e3;this.time=e.toFixed(2),this.accuracy=(this.foundCount/this.words.length*100).toFixed(2),this.saveResults()},async saveResults(){if(!this.authStore.user){alert("Пользователь не авторизован. Пожалуйста, войдите в систему.");return}const e=12,t=parseInt(this.accuracy,10);try{const s=await fetch("http://127.0.0.1:8000/api/result/",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${localStorage.getItem("token")}`},body:JSON.stringify({test:e,user:this.authStore.user.id,score_percentage:t})});if(s.ok)alert("Результаты успешно сохранены!");else{const a=await s.json();console.error("Ошибка сохранения:",a),alert(a.error||"Ошибка при сохранении результатов")}}catch(s){console.error("Ошибка при отправке результатов:",s)}},retryTest(){this.isAnswered=!1,this.selectedOption=null,this.feedback="",this.foundCount=null,this.options=[],this.randomText="",this.testStarted=!1,this.time=0,this.accuracy=0}}},C={class:"container mt-5 text-center"},S={id:"app"},v={class:"container"},A={key:1},O=["innerHTML"],M={key:0,class:"quiz"},N=["onClick"],R={key:0,class:"feedback"},W={key:1,class:"success-message"},L={key:2,class:"results"};function z(e,t,s,a,n,c){const k=h("Navbar"),p=h("router-link");return i(),r(f,null,[m(k),o("div",C,[o("h2",null,d(e.$route.params.name),1),o("div",S,[o("div",v,[t[6]||(t[6]=o("h2",null,"Тест на внимание «Мюнстерберга»",-1)),n.testStarted?(i(),r("div",A,[o("p",{class:"random-text",innerHTML:n.randomText},null,8,O),o("button",{class:"check-button",onClick:t[1]||(t[1]=(...l)=>c.checkWords&&c.checkWords(...l))},"Проверить количество найденных слов"),n.foundCount!==null?(i(),r("div",M,[t[3]||(t[3]=o("h2",null,"Сколько слов было найдено?",-1)),(i(!0),r(f,null,y(n.options,l=>(i(),r("div",{key:l,class:"option"},[o("button",{onClick:B=>c.checkAnswer(l)},d(l),9,N)]))),128)),n.selectedOption!==null?(i(),r("p",R,d(n.feedback),1)):u("",!0)])):u("",!0),n.isAnswered&&n.feedback==="Правильно!"?(i(),r("p",W," Вы нашли "+d(n.foundCount)+" слов(а). ",1)):u("",!0),n.isAnswered?(i(),r("div",L,[o("p",null,"Время выполнения теста: "+d(n.time)+" секунд",1),o("p",null,"Точность: "+d(n.accuracy)+"%",1)])):u("",!0),n.isAnswered&&n.feedback==="Правильно!"?(i(),r("button",{key:3,class:"retry-button",onClick:t[2]||(t[2]=(...l)=>c.retryTest&&c.retryTest(...l))}," Пройти тест еще раз ")):u("",!0),t[5]||(t[5]=o("br",null,null,-1)),m(p,{to:"/tests",class:"btn btn-secondary"},{default:b(()=>t[4]||(t[4]=[_("Назад к тестам")])),_:1})])):(i(),r("button",{key:0,class:"start-button",onClick:t[0]||(t[0]=(...l)=>c.startTest&&c.startTest(...l))}," Играть "))])])])],64)}const F=w(x,[["render",z]]);export{F as default};
