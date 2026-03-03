import { CanActivateFn } from '@angular/router';

export const studenteGuard: CanActivateFn = (route, state) => {
  return true;
};
