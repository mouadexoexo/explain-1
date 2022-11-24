import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DepartementComponent } from './departement/departement.component';
import { DetailDepartementComponent } from './detail-departement/detail-departement.component';

const routes: Routes = [
  { path: 'search', component: DepartementComponent },
  { path: 'departement/:code', component: DetailDepartementComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
