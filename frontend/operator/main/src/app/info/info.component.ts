import { Component, OnInit , ViewChild , AfterViewInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router'
import {ajax} from 'rxjs/ajax'
declare const Chart:any;
@Component({
  selector: 'app-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.css']
})
export class InfoComponent implements OnInit {
  id_sensor:any;
  url:string;
  constructor(private route: ActivatedRoute) { }
    
  ngOnInit() {
     
    this.id_sensor=this.route.snapshot.params.id;
    this.url='/operator/getInfoSensor/?id='+this.id_sensor;
    document.getElementById('iframe').setAttribute('src',this.url);
  }
  
 


}
