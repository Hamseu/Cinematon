import { TestBed } from '@angular/core/testing';

import { Httpserf } from './httpserf';

describe('Httpserf', () => {
  let service: Httpserf;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Httpserf);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
