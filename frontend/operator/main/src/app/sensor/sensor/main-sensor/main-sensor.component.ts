import { Component, OnInit } from '@angular/core';
import {ajax} from 'rxjs/ajax';
@Component({
  selector: 'app-main-sensor',
  templateUrl: './main-sensor.component.html',
  styleUrls: ['./main-sensor.component.css']
})
export class MainSensorComponent implements OnInit {
  listSensor:any;
  constructor() { }

  ngOnInit() {
    this.getUsers();
  }

  getUsers():void{
    ajax("/operator/getListSensor/")
    .subscribe((res)=>{
      if(res.status===200) this.listSensor=res.response;
     
    });
  }

}
