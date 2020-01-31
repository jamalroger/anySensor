import { Routes } from '@angular/router';
import { ProfileComponent } from './profile/profile.component';
import { MainComponent } from './main/main.component';
import { SensorComponent } from './sensor/sensor.component';
import { InfoComponent } from './info/info.component';
import { EditProfileComponent } from './edit-profile/edit-profile.component';
import { HelpComponent } from './help/help.component';
import { PasswordComponent } from './password/password.component'
import { Not404Component } from './not404/not404.component'
import { MainSensorComponent } from './sensor/sensor/main-sensor/main-sensor.component'
import { CreateComponent } from './sensor/create/create.component'
export  var routes : Routes =[
  {path:'',component:ProfileComponent},
  {path:'help',component:HelpComponent},
  {path:'profile',component:ProfileComponent,children:[
                                                           {path:'password',component:PasswordComponent},
                                                           {path:'edit',component:EditProfileComponent}
                                                    ]
  },
  {path:'sensor',component:SensorComponent,children:[   {path:'',component:MainSensorComponent},
                                                         {path:'create',component:CreateComponent},
                                                         {path:'info/:id',component:InfoComponent},
                                                
                                                        ]
   },
   {path:'**',component:Not404Component},
];