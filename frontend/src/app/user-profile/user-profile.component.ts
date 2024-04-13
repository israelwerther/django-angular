import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  clients: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.fetchClients()
  }

  fetchClients() {
    this.http.get<any[]>('http://127.0.0.1:8000/api/clients/list/').subscribe(clients => {
      this.clients = clients;
      console.log('this.clients::: ', this.clients);
    });
  }

}
