# NAME

WebService::Whistle::Pet::Tracker::API - Perl interface to access the Whistle Pet Tracker Web Service

# SYNOPSIS

    use WebService::Whistle::Pet::Tracker::API;
    my $ws   = WebService::Whistle::Pet::Tracker::API->new(email=>$email, password=>$password);
    my $pets = $ws->pets; #isa ARRAY of HASHes
    foreach my $pet (@$pets) {
      print JSON::XS->new->pretty->encode($pet);
    }

# DESCRIPTION

Perl interface to access the Whistle Pet Tracker Web Service.  All methods return JSON payloads that are converted to Perl data structures.  Methods that require authentication will request a token and cache it for the duration of the object.

# CONSTRUCTORS

## new

    my $ws = WebService::Whistle::Pet::Tracker::API->new(email=>$email, password=>$password);

# PROPERTIES

## email

Sets and returns the registered Whistle account email

## password

Sets and returns the registered Whistle account password

# METHODS

## pets

Returns a list of pets as an array reference

    my $pets = $ws->pets;

## device

Returns device data for the given device id as a hash reference

    my $device        = $ws->device('WXX-ABC123');
    my $battery_level = $device->{'battery_level'}; #0-100 charge level

## pet\_dailies

Returns a list of dailies for the given pet id as an array reference

    my $pet_dailies = $ws->pet_dailies($pet_id);

## pet\_daily\_items

Returns a list of the daily items for the given pet id and day number as an array reference

    my $day_number      = int(time/24/60/60) - 1; #yesterday
    my $pet_daily_items = $ws->pet_daily_items($pet_id, $day_number);

## pet\_stats

Returns pet stats for the given pet id as a hash reference

    my $pet_stats = $ws->pet_stats(123456789);

## places

Returns registered places as an array reference

    my $places = $ws->places;

# METHODS (API)

## api

Returns the decoded JSON data from the given web service end point

    my $data = $ws->api('/end_point');

## login

Calls the login service, caches, and returns the response as a hash reference.

## auth\_token

Retrieves the authentication JWT token from the login end point

# ACCESSORS

## ua

Returns an [HTTP::Tiny](https://metacpan.org/pod/HTTP::Tiny) web client user agent

# SEE ALSO

- Python - [https://github.com/RobertD502/whistleaio](https://github.com/RobertD502/whistleaio)
- NodeJS (old api) - [https://github.com/martzcodes/node-whistle](https://github.com/martzcodes/node-whistle)

# AUTHOR

Michael R. Davis

# COPYRIGHT AND LICENSE

MIT License

Copyright (c) 2023 Michael R. Davis
