import { Routes } from '@angular/router';
import { UsersComponent } from './users/users.component';
import { ProfileComponent } from './profile/profile.component';
import { MainComponent } from './main/main.component';
import { SensorComponent } from './sensor/sensor.component';
import { InfoComponent } from './info/info.component';
import { EditProfileComponent } from './edit-profile/edit-profile.component';
import { EditUserComponent } from './edit-user/edit-user.component';
import { InfoUserComponent } from './info-user/info-user.component';
import { HelpComponent } from './help/help.component';
import { PasswordComponent } from './password/password.component'
import { NewUserComponent } from './new-user/new-user.component'
import { Not404Component } from './not404/not404.component'
import { UserComponent } from './users/user/user.component'
import { MainSensorComponent } from './sensor/sensor/main-sensor/main-sensor.component'

export  var routes : Routes =[
  {path:'',component:ProfileComponent},
  {path:'help',component:HelpComponent},
  {path:'profile',component:ProfileComponent,children:[
                                                           {path:'password',component:PasswordComponent},
                                                           {path:'edit',component:EditProfileComponent}
                                                    ]
  },
  {path:'sensor',component:SensorComponent,children:[   {path:'',component:MainSensorComponent},
                                                         {path:'info/:id',component:InfoComponent},
                                                
                                                        ]
   },
  {path:'users',component:UsersComponent,children: [     
                                                         {path:'',component:UserComponent},
                                                         {path:'new',component:NewUserComponent},
                                                         {path:'edit/:id',component:EditUserComponent},
                                                         {path:'info/:id',component:InfoUserComponent},

                                                   ] 
},
{path:'**',component:Not404Component},
];