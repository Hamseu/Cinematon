import { HttpErrorResponse, HttpInterceptorFn } from '@angular/common/http';
import { catchError, switchMap, throwError } from 'rxjs';
import { inject } from '@angular/core';
import { Httpserf } from '../httpserf';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const http = inject(Httpserf);
  const clonedRequest = req.clone({
    withCredentials: true
  });
  if (req.url.includes('/refresh')) {
    return next(clonedRequest);
  }
  return next(clonedRequest).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status == 401) {
        return http.refresh().pipe(
          switchMap(()=> next(clonedRequest))
        );
      }
      return throwError(()=> error);
      
    }
  )
  );
};
