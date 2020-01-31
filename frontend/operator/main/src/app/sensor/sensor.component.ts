import { Component, OnInit } from '@angular/core';
import {ajax}   from 'rxjs/ajax'
import { }    from '@angular/router'
@Component({
  selector: 'app-sensor',
  templateUrl: './sensor.component.html',
  styleUrls: ['./sensor.component.css']
})
export class SensorComponent implements OnInit {

  listSensor:any;
  constructor() { }

  ngOnInit() {
    this.getUsers();
  }

  getUsers():void{
    ajax("/administrator/getListSensor")
    .subscribe((res)=>{
      this.listSensor=res.response;
    })
  }

}
