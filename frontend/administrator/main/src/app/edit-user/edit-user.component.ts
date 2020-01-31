import { Component, OnInit } from '@angular/core';
import {  ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-edit-user',
  templateUrl: './edit-user.component.html',
  styleUrls: ['./edit-user.component.css']
})
export class EditUserComponent implements OnInit {
       id:number;
  constructor(private route : ActivatedRoute) { }

  ngOnInit() {
    this.id= this.route.snapshot.params.id;
  }

}
