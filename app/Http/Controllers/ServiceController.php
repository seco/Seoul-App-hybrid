<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class ServiceController extends Controller
{
    public function servicies(Request $request)
    {
        $servicies = DB::table('servicies');
        if( $request->has('MAXCLASSNM') ) {
            $servicies = $servicies->where('MAXCLASSNM', $request->MAXCLASSNM);
        }
        if( $request->has('MINCLASSNM') ) {
            if ( $request->MINCLASSNM != '' ) {
                $servicies = $servicies->where('MINCLASSNM', $request->MINCLASSNM);
            }
        }
        if( $request->has('AREANM') ) {
            if ( $request->AREANM != '' ) {
                $servicies = $servicies->where('AREANM', $request->AREANM);
            }
        }
        //$services = $services->where('SVCSTATNM', '접수중')->orWhere('SVCSTATNM', '안내중')->get();
        $servicies = $servicies
            ->where('SVCSTATNM', '접수중')
            //->whereIn('SVCSTATNM', ['접수중', '안내중'])
            ->get();
        return $servicies->toJson(JSON_UNESCAPED_UNICODE);
    }

    public function service(Request $request)
    {
        $service = Servicies::where('SVCID', $request->SVCID)->first();
        return $service->toJson(JSON_UNESCAPED_UNICODE);
    }
}
