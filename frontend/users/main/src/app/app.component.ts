import { Component, ViewEncapsulation} from '@angular/core';
import {ajax} from 'rxjs/ajax'
declare const $:any;
declare const M:any;
@Component({
  selector: 'app-root',
  encapsulation: ViewEncapsulation.None,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'main';
  user: any={username:null,email:null};
  listMenu : any =[
   {name:'My Profile',path:'/profile'},
   {name:'Add Sensor',path:'/sensor/create'},
   {name:'List Sensors',path : '/sensor'},
   {name:'See help',path:'/help'},
  ];

   constructor(){
    

   }
   ngOnInit(){
    M.AutoInit();
    ajax('/getInfo/').
    subscribe((data)=>{
     this.user=data.response;
    });
   }

   goBack() {
     
    window.history.back();
  }
  
}
