import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DepartementService } from '../departement.service'

@Component({
  selector: 'app-detail-departement',
  templateUrl: './detail-departement.component.html',
  styleUrls: ['./detail-departement.component.css']
})
export class DetailDepartementComponent implements OnInit{
  code:any;
  epcis:any;
  constructor( private departementService : DepartementService , private route: ActivatedRoute){}

  ngOnInit(): void{
    this.code = this.route.snapshot.paramMap.get('code');
    this.departementService.listEpcibyDepartement(this.code).subscribe((data : any) => {
      this.epcis = data;
      console.log("epcis ",this.epcis);
    })

  }
}
