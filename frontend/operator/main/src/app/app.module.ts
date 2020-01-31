import { BrowserModule } from '@angular/platform-browser';
import { NgModule, Component } from '@angular/core';
import {FormsModule} from '@angular/forms'
import { RouterModule, Routes } from '@angular/router';
import { LoadingBarRouterModule } from '@ngx-loading-bar/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { UsersComponent } from './users/users.component';
import { routes } from './app.routes';
import { SensorComponent } from './sensor/sensor.component';
import { ProfileComponent } from './profile/profile.component';
import { MainComponent } from './main/main.component';
import { InfoComponent } from './info/info.component';
import { EditProfileComponent } from './edit-profile/edit-profile.component';
import { EditUserComponent } from './edit-user/edit-user.component';
import { InfoUserComponent } from './info-user/info-user.component';
import { HelpComponent } from './help/help.component';
import { PasswordComponent } from './password/password.component';
import { NewUserComponent } from './new-user/new-user.component';
import { Not404Component } from './not404/not404.component';
import { UserComponent } from './users/user/user.component';
import { MainSensorComponent } from './sensor/sensor/main-sensor/main-sensor.component'


@NgModule({
  declarations: [
    AppComponent,
    UsersComponent,
    SensorComponent,
    ProfileComponent,
    MainComponent,
    InfoComponent,
    EditProfileComponent,
    EditUserComponent,
    InfoUserComponent,
    HelpComponent,
    PasswordComponent,
    NewUserComponent,
    Not404Component,
    UserComponent,
    MainSensorComponent
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
