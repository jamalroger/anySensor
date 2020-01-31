import { Component, OnInit } from '@angular/core';
import {  NgForm} from '@angular/forms'
import { HttpClient ,HttpHeaders,HttpParams} from '@angular/common/http';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    'Authorization': document.querySelector('input[name=csrfmiddlewaretoken]').getAttribute('value')
  })
};
@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})

export class CreateComponent implements OnInit {
    res:any;
  constructor(private http : HttpClient) {  }

  ngOnInit() {
  }
  

  onSubmit(f :NgForm){
    const params = new HttpParams()
    .set('sensor_name',f.value.sensor_name)
    .set('model',f.value.model)
    .set('poids',f.value.poids)
    .set('date_fab',f.value.date_fab)
    .set('date_exp',f.value.date_exp)
    .set('des',f.value.des);

    this.http.get('/users/createSensor/',{params})
    .subscribe(res=>{
        this.res="sensor Created";
    },error=>{
        this.res="something wrong";

    })

  }

}
