import { Component, OnInit } from '@angular/core';
import {ajax} from 'rxjs/ajax';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
   info:any;
  constructor(private route :ActivatedRoute) { }

  ngOnInit() {

   this.getInfo();
  }
  getInfo():void{
    ajax("/administrator/getInfo/")
    .subscribe((res)=>{
      this.info=res.response[0];
    });
  }

}
