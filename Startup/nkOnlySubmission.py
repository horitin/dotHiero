from hiero.exporters.FnSubmission import Submission
import hiero.core
"""
Adds entry to Render background task for submission of Nuke (.nk) scripts only.
Usage: 

1) Copy to: ~/.hiero/Python/Startup, 
2) On Export dialog, select 'No Transcoding (.nk only)' from 'Render background tasks' list.
"""
class CustomSubmission(Submission):
  def __init__(self):
    Submission.__init__(self)
  
  def addJob(self, jobType, initDict, filePath):
    if jobType == Submission.kNukeRender:
      # filePath is the nuke script in this case
      # We could return a handle to a RenderTask here, in order to track progress in the hiero export queue
      # see site-packages/hiero/exporters/FnLocalNukeRender.py for an example
      return None

    else:
      raise Exception("CustomNukeSubmission.addJob unknown type: " + jobType)

  def initialise(self):
    """
      Called before any jobs are added, can be used to e.g. show a dialog
      to configure the Submission.
      """
    pass
  
  def addJob(self, jobType, initDict, filePath):
    """
      Add a job to the submission.  May return a Task object which should be processed
      by the caller.
      """
    pass
  
  def startTask(self):
    """
      This will be called when the export queue starts processing this submission,
      before any jobs are added.
      """
    pass
  
  def finishTask(self):
    """
      This will be called after jobs have been added.
      """
    pass
  
  def taskStep(self):
    return False

# Register our default submission type
hiero.core.taskRegistry.addSubmission("No Transcoding (.nk only)", CustomSubmission )