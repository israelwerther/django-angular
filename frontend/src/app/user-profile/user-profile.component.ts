import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  players: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.fetchPlayers()
  }

  fetchPlayers() {
    this.http.get<any[]>('http://127.0.0.1:8000/api/players/list/').subscribe(players => {
      this.players = players;
      console.log('this.players::: ', this.players);
    });
  }

}
