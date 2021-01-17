module Main exposing (..)
import Array exposing (Array, get, fromList)
import Html exposing (Html)
import Html.Events exposing (onClick)
import Browser exposing (sandbox)

slides = Array.fromList <|
    [ "This is the first slide"
    , "This is the second slide"
    , "Now the third"
    , "And the fourth and last"
    ]

type alias Model = Int

type Msg = NextSlide
         | LastSlide


init : Model
init = 0

view : Model -> Html Msg
view i = Html.div 
           [ onClick NextSlide ]
           [Html.text <| Maybe.withDefault "" <| get i slides]

update : Msg -> Model -> Model
update msg = case msg of 
    NextSlide -> (+) 1
    LastSlide -> (+) (-1)

main = Browser.sandbox { init=init, view=view, update=update }
