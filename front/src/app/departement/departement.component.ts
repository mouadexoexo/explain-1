import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DepartementService } from '../departement.service'
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-departement',
  templateUrl: './departement.component.html',
  styleUrls: ['./departement.component.css']
})
export class DepartementComponent implements OnInit{
  departements: any;
  epcis:any;
  isDropDownMenu: any=true;
  dropDownTarget: any= "dropDownTarget";

  constructor( private departementService : DepartementService ){}


  ngOnInit(): void{
    this.departementService.listDepartement().subscribe((data : any) => {
      this.departements = data;
      
    })

  }

  onLogoutClick(code:any){
    this.departementService.listEpcibyDepartement(code).subscribe((data : any) => {
      this.epcis = data;
      console.log(this.epcis);
    })
console.log("code ",code)
  }

}
