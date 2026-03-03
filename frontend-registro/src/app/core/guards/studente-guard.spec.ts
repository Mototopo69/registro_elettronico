import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { studenteGuard } from './studente-guard';

describe('studenteGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) =>
    TestBed.runInInjectionContext(() => studenteGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
