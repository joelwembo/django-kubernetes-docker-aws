-module(helloworld).
-export([start/0]).

start()->
   fun_reverse([H|T]) ->
   fun_reverse(T)++[H];
   fun_reverse([]) ->
   [].