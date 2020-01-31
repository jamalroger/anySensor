import { BrowserModule } from '@angular/platform-browser';
import { NgModule, Component } from '@angular/core';
import {FormsModule} from '@angular/forms'
import { RouterModule, Routes } from '@angular/router';
import { LoadingBarRouterModule } from '@ngx-loading-bar/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { routes } from './app.routes';
import { SensorComponent } from './sensor/sensor.component';
import { ProfileComponent } from './profile/profile.component';
import { MainComponent } from './main/main.component';
import { InfoComponent } from './info/info.component';
import { EditProfileComponent } from './edit-profile/edit-profile.component';
import { HelpComponent } from './help/help.component';
import { PasswordComponent } from './password/password.component';
import { Not404Component } from './not404/not404.component';
import { MainSensorComponent } from './sensor/sensor/main-sensor/main-sensor.component';
import { CreateComponent } from './sensor/create/create.component'


@NgModule({
  declarations: [
    AppComponent,
    SensorComponent,
    ProfileComponent,
    MainComponent,
    InfoComponent,
    EditProfileComponent,
    HelpComponent,
    PasswordComponent,
    Not404Component,
    MainSensorComponent,
    CreateComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    LoadingBarRouterModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
