import { Component, OnInit } from '@angular/core';
import {ajax} from 'rxjs/ajax';
@Component({
  selector: 'app-main-sensor',
  templateUrl: './main-sensor.component.html',
  styleUrls: ['./main-sensor.component.css']
})
export class MainSensorComponent implements OnInit {
  listSensor:any;
  checkedSesnsor:any;
  constructor() { }

  ngOnInit() {
    this.getUsers();
    this.checkedSesnsor=[];
     
  }

  getUsers():void{
    ajax("/users/getListSensor/")
    .subscribe((res)=>{
      if(res.status===200) this.listSensor=res.response;
    });
  }

  deleteSensor(){

    for(let el  of this.checkedSesnsor){
        ajax("/users/deleteSensor/?id="+el.id)
        .subscribe((res)=>{
            this.listSensor.splice(el.index,1);
        });
      
    }
    this.checkedSesnsor=[];
  }
checked(id,index){
  let el ={ id:id,index:index};
  if(this.isChecked(el))
        this.checkedSesnsor.splice(this.isChecked(el),1);
  else 
        this.checkedSesnsor.push(el);

      }
isChecked(el){
  for(let i in this.checkedSesnsor){
    if(this.checkedSesnsor[i].id===el.id && el.index===this.checkedSesnsor[i].index)
          return i;
    return 0;
  }
  
}
}