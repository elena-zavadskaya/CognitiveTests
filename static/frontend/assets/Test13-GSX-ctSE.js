import{l as y,h as M,b as m,e as l,o as n,f as v,g as s,t as d,k as c,i as h,F as f,j as B,m as k,w as I}from"./index-CX3mfoam.js";const _={components:{Navbar:M},data(){return{gameStarted:!1,balls:[{x:140,y:0,color:this.getRandomColor(),moving:!0,direction:"down"},{x:0,y:140,color:this.getRandomColor(),moving:!0,direction:"right"}],score:0,speed:2,interval:null,nextBallIndex:0,resultMessage:"",finalMessage:"",level:1}},methods:{startGame(){this.gameStarted=!0,this.score=0,this.level=1,this.speed=2,this.balls.forEach((e,t)=>{e.x=t===0?140:0,e.y=t===0?0:140,e.moving=!0}),this.nextBallIndex=0,this.resultMessage="",this.finalMessage="",this.startInterval()},startInterval(){this.interval=setInterval(()=>{this.moveBalls()},50)},moveBalls(){this.balls.forEach(e=>{e.moving&&(e.direction==="down"?(e.y+=this.speed,e.y>300&&(e.y=0)):e.direction==="up"&&(e.y-=this.speed,e.y<0&&(e.y=300)),e.direction==="right"?(e.x+=this.speed,e.x>300&&(e.x=0)):e.direction==="left"&&(e.x-=this.speed,e.x<0&&(e.x=300)))})},stopNextBall(){if(this.nextBallIndex<this.balls.length){const e=this.balls[this.nextBallIndex];e.moving=!1,this.calculateScore(),this.nextBallIndex++,this.nextBallIndex===this.balls.length&&(this.displayResult(),this.nextLevel())}},calculateScore(){this.balls.forEach(o=>{const u=Math.sqrt((o.x-140)**2+(o.y-140)**2);this.score+=Math.max(0,100-u)})},displayResult(){this.score>1100?this.resultMessage="Отличный уровень координации":this.score>=1e3?this.resultMessage="Средний уровень координации":this.resultMessage="Нуждается в улучшении"},nextLevel(){this.level<3?(this.level++,this.speed+=1,this.resetGame()):(this.finalMessage="Игра завершена! Ваш финальный счет: "+this.score,clearInterval(this.interval))},resetGame(){this.balls.forEach((e,t)=>{e.x=t===0?140:0,e.y=t===0?0:140,e.moving=!0}),this.nextBallIndex=0,this.resultMessage=""},restartGame(){this.startGame()},getRandomColor(){const e="0123456789ABCDEF";let t="#";for(let o=0;o<6;o++)t+=e[Math.floor(Math.random()*16)];return t}},mounted(){},beforeUnmount(){clearInterval(this.interval)}},C={class:"container mt-5 text-center"},N={id:"app"},G={key:0},S={key:1},E={class:"score"},R={class:"level"},w={key:0,class:"result"},L={key:1,class:"final-result"};function V(e,t,o,u,r,a){const x=m("Navbar"),g=m("router-link");return n(),l(f,null,[v(x),s("div",C,[s("h2",null,"Тест №"+d(e.$route.params.id),1),s("div",N,[s("div",null,[r.gameStarted?(n(),l("div",S,[s("div",{class:"game-container",onClick:t[1]||(t[1]=(...i)=>a.stopNextBall&&a.stopNextBall(...i))},[t[5]||(t[5]=s("div",{class:"line vertical"},null,-1)),t[6]||(t[6]=s("div",{class:"line horizontal"},null,-1)),(n(!0),l(f,null,B(r.balls,(i,p)=>(n(),l("div",{key:p,class:"ball",style:k({left:i.x+"px",top:i.y+"px",backgroundColor:i.color})},null,4))),128)),s("div",E,"Score: "+d(r.score),1),s("div",R,"Level: "+d(r.level),1)]),r.resultMessage?(n(),l("div",w,d(r.resultMessage),1)):h("",!0),r.finalMessage?(n(),l("div",L,d(r.finalMessage),1)):h("",!0),r.finalMessage?(n(),l("button",{key:2,onClick:t[2]||(t[2]=(...i)=>a.restartGame&&a.restartGame(...i)),class:"restart-button"},"Начать заново")):h("",!0)])):(n(),l("div",G,[t[3]||(t[3]=s("h2",null,"Тест на зрительно-моторную координацию",-1)),t[4]||(t[4]=s("p",null,[c("В каждом раунде ты увидишь два шарика. Шарики будут двигаться вдоль своей оси, "),s("br"),c(" и твоя цель - заставить их остановиться как можно ближе к пересечению линий.")],-1)),s("button",{onClick:t[0]||(t[0]=(...i)=>a.startGame&&a.startGame(...i)),class:"start-button"},"Начать игру")])),t[8]||(t[8]=s("br",null,null,-1)),t[9]||(t[9]=c()),v(g,{to:"/tests",class:"btn btn-secondary"},{default:I(()=>t[7]||(t[7]=[c("Назад к тестам")])),_:1})])])])],64)}const b=y(_,[["render",V],["__scopeId","data-v-c9c08562"]]);export{b as default};
