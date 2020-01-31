import { Component, OnInit } from '@angular/core';
import {ajax}   from 'rxjs/ajax'
import { }    from '@angular/router'
@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
    listUser:any;
    checkedUser:any;
  constructor() { }

  ngOnInit() {
    this.getUsers();
    this.checkedUser=[];
  }

  getUsers():void{
    ajax("/administrator/getListUsers/")
    .subscribe((res)=>{
      this.listUser=res.response;
    })
  }

  deleteUser(){

    for(let el  of this.checkedUser){
        ajax("/administrator/deleteUser/?id="+el.id)
        .subscribe((res)=>{
            this.listUser.splice(el.index,1);
        });
      
    }
    this.checkedUser=[];
  }
checked(id,index){
  let el ={ id:id,index:index};
  if(this.isChecked(el))
        this.checkedUser.splice(this.isChecked(el),1);
  else 
        this.checkedUser.push(el);

      }
isChecked(el){
  for(let i in this.checkedUser){
    if(this.checkedUser[i].id===el.id && el.index===this.checkedUser[i].index)
          return i;
    return 0;
  }
  
}
}
