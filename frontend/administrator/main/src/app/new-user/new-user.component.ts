import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { HttpHeaders,HttpParams } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { tap } from 'rxjs/operators';


@Component({
  selector: 'app-new-user',
  templateUrl: './new-user.component.html',
  styleUrls: ['./new-user.component.css']
})
export class NewUserComponent implements OnInit {
      res:any;
         
  constructor(private httpClient:HttpClient) { }

  ngOnInit() {
    this.res="";
  }

  onSubmit(f: NgForm) {
    const params = new HttpParams()
    .set('username',f.value.username)
    .set('password', f.value.password)
    .set('first_name', f.value.first_name)
    .set('last_name', f.value.last_name)
    .set('cin', f.value.cin)
    .set('email', f.value.email)
    .set('tel', f.value.tel)
    .set('job', f.value.job)
    .set('adresse', f.value.adresse)
    .set('city', f.value.city)
    .set('dn', f.value.dn);

    if(f.value.password!=f.value.password2 || f.value.password===""){
         this.res="passowrd are not equal or Null";
         return ;
    }
    if(!f.value.dn){
         this.res="Type The Birthday";
         return ;
    }  
    this.httpClient.get("/administrator/createUser/",{params})
    .subscribe(
      data=>{  this.res="User Created";  }
      ,
      error=>{  this.res="User Created";  }
    );

  }

}
