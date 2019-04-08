import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NerdFightComponent } from './nerd-fight.component';

describe('NerdFightComponent', () => {
  let component: NerdFightComponent;
  let fixture: ComponentFixture<NerdFightComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NerdFightComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NerdFightComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
