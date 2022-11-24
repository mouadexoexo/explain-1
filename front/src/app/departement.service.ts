import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Departement} from './departement.model';
import { DetailDepartement } from 'DetailDepartement.model';

@Injectable({
  providedIn: 'root'
})
export class DepartementService {

  baseUrl:string ='http://127.0.0.1:5000/'

  constructor(private httpClient : HttpClient) { }


  public listDepartement(){
    return this.httpClient.get<Departement[]>(this.baseUrl+'departements')
  }
  public listEpcibyDepartement(codeDep:any){
    return this.httpClient.get<DetailDepartement[]>(this.baseUrl+'FRDEPA'+codeDep)
  }
}
