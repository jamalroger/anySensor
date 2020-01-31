import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router'
import {ajax} from 'rxjs//ajax'

@Component({
  selector: 'app-info-user',
  templateUrl: './info-user.component.html',
  styleUrls: ['./info-user.component.css']
})
export class InfoUserComponent implements OnInit {
    id_user:number;
    info:any;
    listSensor:any;
  constructor(private route: ActivatedRoute ) { }
  ngOnInit() {
    this.id_user=this.route.snapshot.params.id;
    ajax('/operator/getInfo/?id='+this.id_user)
    .subscribe(data=>{
      this.info=data.response[0];
    });
    ajax('/operator/getListSensorOf/?id='+this.id_user)
    .subscribe(data=>{
      this.listSensor=data.response;
    });
  }


}
