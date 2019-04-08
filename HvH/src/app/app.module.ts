import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import {
  MatToolbarModule,
  MatButtonModule,
  MatFormFieldModule,
  MatInputModule,
  MatTableModule
} from '@angular/material';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './component/home-page/home-page.component';
import { BattlePageComponent } from './component/battle-page/battle-page.component';
import { NerdFightComponent } from './component/nerd-fight/nerd-fight.component';
import { HeaderComponent } from './component/header/header.component';


const routes = [
  { path: 'home', component: HomePageComponent },
  { path: 'battle', component: BattlePageComponent },
  { path: 'nerdFight', component: NerdFightComponent },
  { path: '**', component: HomePageComponent }
]


@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    BattlePageComponent,
    NerdFightComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(routes),
    MatToolbarModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
