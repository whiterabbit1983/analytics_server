import json
from dateutil.parser import parse
from recommend import predict


class AnalyticsService:
    exposed = True

    def POST(self, data, algo, current_date):
        try:
            data = json.loads(data)
        except Exception as exc:
            return json.dumps({'error': str(exc)})
        else:
            res_dates = {}
            for item, dates in list(data.items()):
                res_dates[item] = [parse(d) for d in dates]

            return json.dumps(
                predict(
                    res_dates,
                    algo=algo,
                    current_date=parse(current_date)
                )
            )
