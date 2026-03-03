import { CanActivateFn } from '@angular/router';

export const docenteGuard: CanActivateFn = (route, state) => {
  return true;
};
