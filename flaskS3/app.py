from flask import Flask, render_template, request, redirect, url_for, flash, Response,session
from flask_bootstrap import Bootstrap
from config import S3
from filters import date_timeformat, file_type

app = Flask(__name__)
Bootstrap(app)
app.jinja_env.filters['Hdatetimeformat'] = date_timeformat
app.jinja_env.filters['file_type'] = file_type

# First Get all the Keys From the Config File
s3config = S3.get_config()
app.secret_key = s3config.APP_SECRET_KEY

@app.route('/')
def index():
    session.clear()
    buckets = S3.get_buckets_list()
    return render_template("index.html", buckets=buckets)

@app.route('/files/<bucket>',methods = ['GET','POST'])
def files(bucket):
    if bucket == 'DUMMY':
        return render_template('files.html', my_bucket='', files='')
    session['bucket'] = bucket
    s3_resource = S3.get_resource()
    my_bucket = s3_resource.Bucket(bucket)
    summaries = my_bucket.objects.all()
    return render_template('files.html', my_bucket=my_bucket, files=summaries)

@app.route('/upload', methods = ['GET','POST'])
def upload():
    try:
        file = request.files['filename']
    except KeyError:
        flash('No File Selected')
        return redirect(url_for('files', bucket = session.get('bucket','DUMMY')))
    except:
        flash('No File Selected')
        return redirect(url_for('files', bucket = session.get('bucket','DUMMY')))

    s3_resource = S3.get_resource()
    my_bucket = s3_resource.Bucket(session.get('bucket'))
    my_bucket.Object(file.filename).put(Body=file)
    flash('Files Uploaded Sucessfully')

    return redirect(url_for('files', bucket = session.get('bucket','DUMMY')))



@app.route('/delete', methods = ['POST'])
def delete():
    key = request.form['key']
    print('File Name ---->',key)
    s3_resource = S3.get_resource()
    my_bucket = s3_resource.Bucket(session.get('bucket'))
    my_bucket.Object(key).delete()
    flash('File deleted successfully')

    return redirect(url_for('files' , bucket = session.get('bucket','DUMMY')))


@app.route('/download', methods = ['POST'])
def download():
    key = request.form['key']
    print('Download File Name ----> {}').format(key)
    s3_resource = S3.get_resource()
    my_bucket   = s3_resource.Bucket(session.get('bucket'))

    file_obj = my_bucket.Object(key).get()


    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
        )

if __name__== '__main__' :
    app.run()
