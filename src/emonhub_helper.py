
import urllib2
import httplib
import time
import logging
import threading

"""class EmonHubHelper


"""

class EmonHubHelper(threading.Thread):

    def __init__(self, helperName, queue, **kwargs):
        """Create a helper thread."""

        # Initialize logger
        self._log = logging.getLogger("EmonHub")

        # Initialise thread
        threading.Thread.__init__(self)
        self.name = helperName

        # initialise settings
        self._settings = {'interval': '', 'pause': '', 'urlstring': ''}

        # Initialize interval timer's "started at" timestamp
        self._interval_timestamp = 0

        # Initialise the queue
        self._queue = queue

        # Start the helper thread
        self.stop = False
        self.start()


    def run(self):
        """
        Run the helper thread.

        """
        while not self.stop:
            # Don't loop to fast
            time.sleep(0.1)
            # Action reporter tasks
            self.action()


    def action(self):
        """

        """

        # pause if 'pause' set to 'all' or 'in'
        if 'pause' in self._settings \
                and str(self._settings['pause']).lower() in ['all', 'in']:
            return

        # Check if the required interval has passed since last run
        if int(self._settings['interval']) \
                and time.time() - self._interval_timestamp < int(self._settings['interval']):
            return

        # Reset timer
        self._interval_timestamp = time.time()

        # Then attempt to fetch the data
        self._get_data(self._settings['urlstring'])


    def _get_data(self, req_url):
        """

        """

        try:
            request = urllib2.urlopen(req_url, timeout=60)
            retrieved = request.read()
        except ValueError as e:
            self._log.warning(self.name + " couldn't retrieve data, ValueError: " +
                              str(e.message))
        except urllib2.HTTPError as e:
            self._log.warning(self.name + " couldn't retrieve data, HTTPError: " +
                              str(e.code))
        except urllib2.URLError as e:
            self._log.warning(self.name + " couldn't retrieve data, URLError: " +
                              str(e.reason))
        except httplib.HTTPException:
            self._log.warning(self.name + " couldn't retrieve data, HTTPException")
        except Exception:
            import traceback
            self._log.warning(self.name + " couldn't retrieve data, Exception: " +
                              traceback.format_exc())
        else:
            request.close()
            self._queue.put(retrieved)


